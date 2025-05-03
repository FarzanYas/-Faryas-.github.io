import pyhtml as p
from flask import Flask

app = Flask(__name__)

@app.get("/")
def homepage():
    response = p.html(
        p.head(
            p.style("""
                body {
                    background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                                    url("https://thumbs.dreamstime.com/b/perfect-strike-cropped-shot-ethnic-young-man-cricket-attire-isolated-black-256682364.jpg");
                    background-repeat: no-repeat;
                    background-size: cover;
                    background-attachment: fixed;
                    background-position: center;
                    font-family: 'Arial', sans-serif;
                    margin: 0;
                    padding: 20px;
                    min-height: 100vh;
                    color: white;
                    text-align: center;
                }
                
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 30px;
                    background-color: rgba(0, 0, 0, 0.6);
                    border-radius: 15px;
                    box-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
                    backdrop-filter: blur(5px);
                }
                
                h1 {
                    font-size: 3rem;
                    color: #FFD700;
                    text-transform: uppercase;
                    margin-bottom: 30px;
                    text-shadow: 2px 2px 4px #000000;
                    letter-spacing: 2px;
                    font-weight: bold;
                }
                
                ul {
                    list-style-type: none;
                    padding: 0;
                    margin: 0 auto;
                    max-width: 600px;
                }
                
                li {
                    font-size: 1.5rem;
                    margin-bottom: 20px;
                    padding: 15px;
                    background-color: rgba(255, 215, 0, 0.1);
                    border-left: 4px solid #FFD700;
                    border-radius: 0 8px 8px 0;
                    text-align: left;
                    transition: all 0.3s ease;
                }
                
                li:hover {
                    transform: translateX(10px);
                    background-color: rgba(255, 215, 0, 0.2);
                }
                
                .highlight {
                    font-weight: bold;
                    color: #FFD700;
                }
            """)
        ),
        p.body(
            p.div(
                p.h1("The One and Only Cricket Minigames!!"),
                p.ul(
                    p.li("There are two games to choose from, ", p.span("Captain's Corner"), ", or ", p.span("Fantasy Game"), "!"),
                    p.li("Young players can develop their passion for cricket through these exciting apps!!"),
                )
            )
        )
    )
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
