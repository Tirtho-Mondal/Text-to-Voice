from flask import Flask, request, jsonify, send_file, render_template
from ai_integration import text_to_bangla_voice

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the homepage with a form to input text.
    """
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text_to_bangla_voice():
    """
    API endpoint to convert English text to Bengali voice.
    """
    try:
        # Get text input from the form or JSON
        text = request.form.get('text') or request.get_json().get('text')
        
        if not text:
            return jsonify({"error": "Invalid input. Please provide text to convert."}), 400
        
        output_file = "output.mp3"
        
        # Convert text to Bengali voice
        text_to_bangla_voice(text, output_file)
        
        # Return the audio file as a response
        return send_file(output_file, mimetype='audio/mpeg', as_attachment=True)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
