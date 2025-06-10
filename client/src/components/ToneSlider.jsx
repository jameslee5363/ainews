import React from "react";

const labels = ["Liberal", "Center", "Conservative"];

export default function ToneSlider({ value, onChange }) {
  return (
    <div className="tone-slider">
      <input
        type="range"
        min="0"
        max="2"
        step="1"
        value={value}
        onChange={(e) => onChange(Number(e.target.value))}
      />
      <div className="tone-labels">
        {labels.map((label) => (
          <span key={label}>{label}</span>
        ))}
      </div>
    </div>
  );
}
