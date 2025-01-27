style = """
<style>
/* Use entire viewport, disallow scrolling (may hide overflow on very small screens) */
html, body, #app, .nicegui-content {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    box-sizing: border-box;
}

/* Fullscreen gradient background, horizontally center items, stick them at top vertically */
.gradient-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #7F53AC 0%, #647DEE 100%);
    display: flex;
    justify-content: center;  /* Center horizontally */
    align-items: flex-start;  /* Top alignment vertically */
}

/* Main container on top of gradient, centered within the page */
.main-container {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    align-items: center;      /* Center content in this column */
    max-width: 800px;
    width: 100%;
    margin: 2rem auto 0 auto; /* 2rem from top, then auto left/right centers container horizontally */
    gap: 1rem;
}

/* Title row: icon + text side-by-side, centered horizontally */
.title-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
}

/* Glassy card styling */
.glass-card {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.18);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    width: 100%;
    margin: 0;
    padding: 1rem;
    color: #fff;
}

.hover-scale {
    transition: transform 0.25s ease-in-out;
}
.hover-scale:hover {
    transform: scale(1.02);
}

/* Input styling */
.animated-input {
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
    border: 2px solid #e2e2e2 !important;
    border-radius: 8px !important;
    background-color: #fff !important;
    color: #000 !important; /* black text inside input */
}
.animated-input:focus {
    border-color: #FF8C42 !important;
    box-shadow: 0 0 0 3px rgba(255, 140, 66, 0.25) !important;
}

/* Buttons */
.primary-button {
    background-color: #FF8C42 !important;
    color: #fff !important;
    font-weight: 600 !important;
    transition: background-color 0.2s ease, transform 0.2s ease;
}
.primary-button:hover {
    background-color: #e67b36 !important;
    transform: translateY(-1px);
}

.secondary-button {
    background-color: transparent !important;
    color: #fff !important;
    border: 2px solid #fff !important;
    font-weight: 600 !important;
    transition: border-color 0.2s ease, color 0.2s ease, transform 0.2s ease;
}
.secondary-button:hover {
    border-color: #FFD452 !important;
    color: #FFD452 !important;
    transform: translateY(-1px);
}

/* Shortened URL result card transitions */
.result-card {
    transition: all 0.3s ease;
    overflow: hidden;
    margin-top: 0.5rem;
}
.result-card.hidden {
    opacity: 0;
    max-height: 0;
    margin-top: 0;
}
.result-card.visible {
    opacity: 1;
    max-height: 250px;
}

/* Links in the result card stand out in gold */
.result-card a {
    color: #FFD452 !important;
    text-decoration: none;
}
.result-card a:hover {
    text-decoration: underline;
}

/* Make the "Shortened URL" label bigger and bolder */
.label-shortened-url {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

/* Slightly increase the link text size */
.result-link {
    font-size: 1.125rem; /* ~18px */
    font-weight: 500;
}

/* Row used for link + buttons: spaced and aligned neatly */
.short-url-row {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 0.5rem;
}

/* Container for copy/test buttons so they align to the right properly */
.short-url-buttons {
    display: flex;
    gap: 0.5rem;
    align-items: center;
}

/* Statistics styling */
.stats-title {
    color: #fff;
    font-size: 1.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 0.5rem;
}
.stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    width: 100%;
}
.stats-number {
    color: #FFD452;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 0.25rem;
    text-align: center;
}
.stats-label {
    color: #fff;
    font-size: 0.9rem;
    opacity: 0.9;
    text-align: center;
}

/* Responsive for small screens */
@media (max-width: 600px) {
    .stats-grid {
        grid-template-columns: 1fr;
    }
    .short-url-row {
        flex-direction: column;
        align-items: flex-start;
    }
}
</style>
"""