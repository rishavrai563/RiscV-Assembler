from flask import Flask, render_template, request, send_file, Response
import subprocess
import os
import tempfile

# Initialize Flask app.
# We no longer need 'static_folder' as all CSS is in index.html.
app = Flask(__name__, template_folder="web/templates")

# Check OS to find the correct assembler executable name
# Use 'assembler.exe' on Windows, 'assembler.out' on Linux/macOS
assembler_name = "assembler.exe" if os.name == 'nt' else "assembler.out"
ASSEMBLER_PATH = os.path.join("src", assembler_name)

# Helper function to check if the assembler is compiled
def check_assembler():
    if not os.path.exists(ASSEMBLER_PATH):
        print("="*50)
        print(f"ERROR: Assembler executable not found.")
        print(f"Please compile it first by running:")
        print(f"  cd src")
        print(f"  g++ assembler.cpp -o {assembler_name} -std=c++20")
        print(f"  cd ..")
        print("="*50)
        return False
    return True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if not check_assembler():
        return f"Assembler not found at {ASSEMBLER_PATH}. Check server logs.", 500

    if "file" not in request.files:
        return "No file uploaded", 400

    asm_file = request.files["file"]
    if asm_file.filename == "":
        return "Empty filename", 400

    # Save uploaded .asm file temporarily
    with tempfile.TemporaryDirectory() as tempdir:
        # Use a fixed, safe filename inside the temp directory
        asm_path = os.path.join(tempdir, "input.asm")
        mc_path = os.path.join(tempdir, "output.mc")
        
        asm_file.save(asm_path)

        # Run your assembler executable
        try:
            # Use capture_output=True to get stdout/stderr
            # This allows sending C++ errors back to the user
            process = subprocess.run(
                [ASSEMBLER_PATH, asm_path, mc_path], 
                check=True, 
                capture_output=True, 
                text=True,
                timeout=10 # Add 10-second timeout for safety
            )
        
        except subprocess.CalledProcessError as e:
            # Assembler failed (e.g., syntax error)
            # Return the error message from the assembler itself
            error_output = e.stderr or e.stdout or "Unknown assembler error"
            return f"Assembler Failed:\n{error_output}", 500
        except subprocess.TimeoutExpired:
            return "Assembler process timed out.", 500
        except Exception as e:
            return f"An unexpected error occurred: {e}", 500

        # Check if the output file was created
        if not os.path.exists(mc_path):
            return "Assembler ran but produced no output file.", 500

        # Read the file content into memory
        try:
            with open(mc_path, 'r') as f:
                mc_content = f.read()
        except Exception as e:
            return f"Error reading output file: {e}", 500
            
        # Now that the file is read and its handle is closed, 
        # the 'with tempfile.TemporaryDirectory()' can safely delete
        # the file when the block exits.
        
        # Return the content directly as a response
        return Response(mc_content, mimetype='text/plain')

if __name__ == "__main__":
    check_assembler() # Check on startup
    app.run(debug=True)