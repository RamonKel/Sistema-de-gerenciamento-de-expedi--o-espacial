from app import app
import os

if __name__== '__main__':
  port = int(os.getenv('PORT', 5000))
  app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    app.run(debug=True)
