import React, { useState } from "react";
import "./ScanPage.css";

function ScanPage() {
  const [iPhoneCapture, setIPhoneCapture] = useState(null);
  const [depthCapture, setDepthCapture] = useState(null);

  const handleIPhoneUpload = (event) => {
    setIPhoneCapture(event.target.files[0]);
  };

  const handleDepthUpload = (event) => {
    setDepthCapture(event.target.files[0]);
  };

  return (
    <div className="scan-page">
      <nav className="navbar">
        <div className="logo">
          <h1>3DScan</h1>
        </div>
      </nav>

      <div className="upload-container">
        <div className="upload-section">
          <h2>iPhone Capture</h2>
          <div className="upload-box">
            <input
              type="file"
              accept="image/*"
              onChange={handleIPhoneUpload}
              id="iphone-upload"
            />
            <label htmlFor="iphone-upload">
              {iPhoneCapture ? iPhoneCapture.name : "Upload iPhone Capture"}
            </label>
          </div>
        </div>

        <div className="upload-section">
          <h2>Depth Camera Capture</h2>
          <div className="upload-box">
            <input
              type="file"
              accept="image/*"
              onChange={handleDepthUpload}
              id="depth-upload"
            />
            <label htmlFor="depth-upload">
              {depthCapture ? depthCapture.name : "Upload Depth Camera Capture"}
            </label>
          </div>
        </div>

        <div className="point-cloud-section">
          <h2>Point Cloud Visualization</h2>
          <div className="point-cloud-container">
            {/* Point cloud will be rendered here */}
            <p>Point cloud visualization will appear here after processing</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ScanPage;
