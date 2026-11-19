# This is app.py from python
from flask import Flask, render_template_string
import platform
import datetime
import socket

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Noor | Welcome</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Amiri:wght@400;700&display=swap" rel="stylesheet">

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', sans-serif;
    min-height: 100vh;
    color: white;
    background: linear-gradient(135deg, #071c25, #103d36, #092d36);
    overflow-x: hidden;
}

/* Background decoration */
body::before {
    content: "";
    position: fixed;
    width: 450px;
    height: 450px;
    background: #00e6a0;
    filter: blur(180px);
    opacity: .18;
    top: -150px;
    right: -100px;
}

body::after {
    content: "";
    position: fixed;
    width: 400px;
    height: 400px;
    background: #d6a84f;
    filter: blur(180px);
    opacity: .15;
    bottom: -150px;
    left: -100px;
}

.container {
    position: relative;
    z-index: 1;
    max-width: 1100px;
    margin: auto;
    padding: 35px 20px;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 35px;
}

.logo {
    font-size: 25px;
    font-weight: 700;
    color: #e9c875;
}

.logo span {
    color: #fff;
}

.nav-tag {
    border: 1px solid #ffffff35;
    padding: 9px 18px;
    border-radius: 30px;
    font-size: 12px;
    color: #d8e9e2;
}

.hero {
    text-align: center;
    padding: 55px 15px 45px;
}

.moon {
    font-size: 65px;
    color: #eacb76;
    margin-bottom: 15px;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-12px); }
}

.arabic {
    font-family: 'Amiri', serif;
    font-size: clamp(35px, 7vw, 58px);
    color: #f1d58c;
    margin-bottom: 12px;
}

.hero h1 {
    font-size: clamp(30px, 5vw, 48px);
    font-weight: 600;
    margin-bottom: 12px;
}

.hero h1 span {
    color: #e9c875;
}

.hero p {
    color: #b8d1c9;
    font-size: 14px;
    letter-spacing: 1px;
}

.divider {
    width: 90px;
    height: 3px;
    background: linear-gradient(90deg, transparent, #eacb76, transparent);
    margin: 25px auto;
}

.quote {
    max-width: 700px;
    margin: auto;
    text-align: center;
    padding: 25px;
    background: #ffffff0c;
    border: 1px solid #ffffff20;
    border-radius: 18px;
    backdrop-filter: blur(15px);
}

.quote p {
    color: #f1d58c;
    font-family: 'Amiri', serif;
    font-size: 25px;
}

.quote small {
    color: #b8d1c9;
    display: block;
    margin-top: 10px;
}

.section-title {
    margin: 45px 0 20px;
    font-size: 20px;
    color: #e9c875;
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 18px;
}

.card {
    padding: 25px;
    border-radius: 18px;
    background: #ffffff0d;
    border: 1px solid #ffffff20;
    backdrop-filter: blur(15px);
    transition: .3s ease;
}

.card:hover {
    transform: translateY(-8px);
    border-color: #e9c875;
    background: #ffffff17;
}

.card .icon {
    font-size: 32px;
    margin-bottom: 15px;
}

.card h3 {
    font-size: 17px;
    margin-bottom: 8px;
    color: #f1d58c;
}

.card p {
    font-size: 12px;
    color: #b8d1c9;
    line-height: 1.8;
}

.info {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 15px;
    margin-top: 25px;
}

.info-box {
    background: #ffffff0d;
    border-radius: 14px;
    padding: 18px;
    border: 1px solid #ffffff15;
}

.info-box span {
    display: block;
    color: #9bbdb2;
    font-size: 12px;
    margin-bottom: 7px;
}

.info-box strong {
    color: #e9c875;
    font-size: 15px;
    overflow-wrap: anywhere;
}

footer {
    text-align: center;
    margin-top: 55px;
    padding: 25px;
    border-top: 1px solid #ffffff20;
    color: #9bbdb2;
    font-size: 12px;
}

footer span {
    color: #e9c875;
}

@media(max-width: 600px) {
    .hero { padding-top: 35px; }
    nav { padding-bottom: 15px; }
    .container { padding: 20px 15px; }
}
</style>
</head>

<body>

<div class="container">

<nav>
    <div class="logo">☪ NOOR<span>.</span></div>
    <div class="nav-tag">✦ PEACE • FAITH • HOPE</div>
</nav>

<section class="hero">

    <div class="moon">☾</div>

    <div class="arabic">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>

    <h1>Welcome to <span>Noor</span></h1>

    <p>A LITTLE LIGHT CAN BRIGHTEN THE WORLD</p>

    <div class="divider"></div>

</section>

<div class="quote">
    <p>فَإِنَّ مَعَ الْعُسْرِ يُسْرًا</p>
    <small>Indeed, with hardship comes ease. — Quran 94:5</small>
</div>

<h2 class="section-title">✦ Discover the Beauty of Islam</h2>

<section class="cards">

    <div class="card">
        <div class="icon">🕌</div>
        <h3>Prayer & Faith</h3>
        <p>Find peace and strength through prayer, patience and faith in Allah.</p>
    </div>

    <div class="card">
        <div class="icon">📖</div>
        <h3>Quran & Knowledge</h3>
        <p>Explore the wisdom, guidance and beautiful teachings of the Holy Quran.</p>
    </div>

    <div class="card">
        <div class="icon">🤲</div>
        <h3>Dua & Gratitude</h3>
        <p>Remember Allah, express gratitude and keep your heart full of hope.</p>
    </div>

    <div class="card">
        <div class="icon">🌙</div>
        <h3>Peace & Blessings</h3>
        <p>Spread kindness, compassion and love in everything you do.</p>
    </div>

</section>

<h2 class="section-title">✦ Server Information</h2>

<section class="info">

    <div class="info-box">
        <span>SERVER HOSTNAME</span>
        <strong>{{ hostname }}</strong>
    </div>

    <div class="info-box">
        <span>OPERATING SYSTEM</span>
        <strong>{{ system }}</strong>
    </div>

    <div class="info-box">
        <span>PYTHON VERSION</span>
        <strong>{{ python }}</strong>
    </div>

    <div class="info-box">
        <span>SERVER TIME</span>
        <strong id="clock">{{ server_time }}</strong>
    </div>

</section>

<footer>
    Made with <span>♥</span> and gratitude to Allah
    <br><br>
    © 2026 NOOR | Powered by Python & Flask
</footer>

</div>

<script>
function updateClock() {
    document.getElementById("clock").textContent =
        new Date().toLocaleString();
}
updateClock();
setInterval(updateClock, 1000);
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        hostname=socket.gethostname(),
        system=f"{platform.system()} {platform.release()}",
        python=platform.python_version(),
        server_time=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    )

@app.route("/health")
def health():
    return {"status": "healthy", "application": "Noor"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
