console.log('THANKS FOR USING BEST CSS');
const paintCanvas = document.getElementById('paintCanvas');
const canvasPaint = paintCanvas.getContext('2d');
paintCanvas.width = window.innerWidth - 50;
paintCanvas.height = window.innerHeight - 50;
let painting = false;
function startPosition(e) {
    painting = true;
    draw(e);
}
function endPosition() {
    painting = false;
    canvasPaint.beginPath();
}
function draw(e) {
    if (!painting) return;
    canvasPaint.lineWidth = 5; 
    canvasPaint.lineCap = 'round'; 
    canvasPaint.strokeStyle = '#000'; 
    canvasPaint.lineTo(e.clientX - paintCanvas.offsetLeft, e.clientY - paintCanvas.offsetTop);
    canvasPaint.stroke();
    canvasPaint.beginPath();
    canvasPaint.moveTo(e.clientX - paintCanvas.offsetLeft, e.clientY - paintCanvas.offsetTop);
}
paintCanvas.addEventListener('mousedown', startPosition);
paintCanvas.addEventListener('mouseup', endPosition);
paintCanvas.addEventListener('mousemove', draw);
const blueCursorCircleBirNeon = document.querySelector('.blue-cursor-circle-bir-neon');
document.addEventListener('mousemove', (e) => {
    blueCursorCircleBirNeon.style.left = `${e.pageX}px`;
    blueCursorCircleBirNeon.style.top = `${e.pageY}px`;
    const smoke = document.createElement('div');
    smoke.className = 'smoke';
    smoke.style.left = `${e.pageX - 30}px`;
    smoke.style.top = `${e.pageY - 30}px`;
    document.body.appendChild(smoke);
    setTimeout(() => {
        smoke.remove();
    }, 600);
});
document.addEventListener('mouseenter', () => {
    blueCursorCircleBirNeon.classList.add('active');
});
document.addEventListener('mouseleave', () => {
    blueCursorCircleBirNeon.classList.remove('active');
});
document.head.appendChild(style);
const cursor = document.querySelector('.cursor-circle');
        window.addEventListener('mousemove', (event) => {
            cursor.style.left = event.clientX - 50 + 'px';
            cursor.style.top = event.clientY - 50 + 'px';
            const red = Math.floor(Math.random() * 256);
            const green = Math.floor(Math.random() * 256);
            const blue = Math.floor(Math.random() * 256);
            cursor.style.backgroundColor = `rgba(${red}, ${green}, ${blue}, 0.1)`;
        });
document.addEventListener('mousemove', function(e) {
    const cursor = document.querySelector('.blue-circle-cursor');
    cursor.style.left = e.pageX + 'px';
    cursor.style.top = e.pageY + 'px';
});
document.addEventListener('mousemove', function(e) {
    const cursor = document.querySelector('.red-circle-cursor');
    cursor.style.left = e.pageX + 'px';
    cursor.style.top = e.pageY + 'px';
});
document.addEventListener('mousemove', function(e) {
    const cursor = document.querySelector('.green-circle-cursor');
    cursor.style.left = e.pageX + 'px';
    cursor.style.top = e.pageY + 'px';
});
document.addEventListener('mousemove', function(e) {
    const cursor = document.querySelector('.black-circle-cursor');
    cursor.style.left = e.pageX + 'px';
    cursor.style.top = e.pageY + 'px';
});
document.addEventListener('mousemove', function(e) {
    const cursor = document.querySelector('.white-circle-cursor');
    cursor.style.left = e.pageX + 'px';
    cursor.style.top = e.pageY + 'px';
});
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;
themeToggle.addEventListener('click', () => {
  if (body.classList.contains('dark-mode')) {
    body.classList.remove('dark-mode');
    body.classList.add('light-mode');
    themeToggle.textContent = 'Dark Mode';
  } else {
    body.classList.remove('light-mode');
    body.classList.add('dark-mode');
    themeToggle.textContent = 'Light Mode';
  }
});
function blackAlert() {
    const alertDiv = document.getElementById('alert');
    alertDiv.style.display = 'block';
    setTimeout(() => {
        alertDiv.style.display = 'none';
    }, 3000);
}
function showDangerAlert() {
    const alertDiv = document.querySelector('.danger-alert');
    alertDiv.style.display = 'block';
    setTimeout(() => {
        alertDiv.style.display = 'none';
    }, 3000);
}
function greenAlert() {
    const alertDiv = document.querySelector('.green-alert');
    alertDiv.style.display = 'block';
    setTimeout(() => {
        alertDiv.style.display = 'none';
    }, 3000);
}
function blueAlert() {
    const alertDiv = document.querySelector('.blue-alert');
    alertDiv.style.display = 'block';
    setTimeout(() => {
        alertDiv.style.display = 'none';
    }, 3000);
}
function errorAlert() {
    const alertDiv = document.querySelector('.error-alert');
    const iconSpan = alertDiv.querySelector('.icon');
    iconSpan.textContent = '❗';

    alertDiv.style.display = 'block';
    setTimeout(() => {
        alertDiv.style.display = 'none';
    }, 3000);
}
const button = document.querySelector('.black-button');

button.addEventListener('mouseover', () => {
  button.style.transform = 'translateZ(10px) rotateY(10deg)';
  button.style.boxShadow = '0 0 20px rgba(255, 255, 255, 0.4)';
});

button.addEventListener('mouseout', () => {
  button.style.transform = 'translateZ(0) rotateY(0deg)';
  button.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.2)';
});

button.addEventListener('mousedown', () => {
  button.style.transform = 'translateZ(10px) rotateY(10deg) scale(0.95)';
  button.style.boxShadow = '0 0 8px rgba(255, 255, 255, 0.3)';
});

button.addEventListener('mouseup', () => {
  button.style.transform = 'translateZ(10px) rotateY(10deg)';
  button.style.boxShadow = '0 0 20px rgba(255, 255, 255, 0.4)';
});
const borderElement = document.querySelector('.border');
const emojiCount = 15;
const emoji = '🌍';
borderElement.innerHTML = emoji.repeat(emojiCount);
function clickShow() {
    const clickShowDiv = document.querySelector('.click-show');
    clickShowDiv.style.display = clickShowDiv.style.display === 'none' || clickShowDiv.style.display === '' ? 'block' : 'none';
}
function showSection(sectionId) {
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        section.style.display = 'none';
    });
    const selectedSection = document.getElementById(sectionId);
    selectedSection.style.display = 'block';
}
showSection('spa-section1');
console.error = function() {};