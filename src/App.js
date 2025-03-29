import "./App.css";

function App() {
  return (
    <div className="App">
      <nav className="navbar">
        <div className="logo">
          <h1>3DScan</h1>
        </div>
        <div className="nav-links">
          <a href="/scan" className="start-scan-btn">
            Start Scanning
          </a>
        </div>
      </nav>

      <main className="hero-section">
        <div className="hero-content">
          <h1>Transform Reality into Digital 3D</h1>
          <p>
            Create professional 3D models instantly using your iPhone or iPad's
            advanced sensors
          </p>
          <div className="cta-buttons">
            <button className="primary-btn">Try for free</button>
            <button className="secondary-btn">About us</button>
          </div>
        </div>

        <div className="feature-cards">
          <div className="feature-card">
            <div className="feature-icon">📱</div>
            <h3>LiDAR Scanning</h3>
            <p>Precise 3D space mapping with iOS LiDAR technology</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🔄</div>
            <h3>360° Photos</h3>
            <p>Capture immersive panoramic scenes in full detail</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🎨</div>
            <h3>3D Models</h3>
            <p>Generate detailed 3D models from simple photos</p>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
