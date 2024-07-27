const input = document.getElementById('img-upload');
const preview = document.getElementById('img-preview');

input.addEventListener('input', () => {
  const url = URL.createObjectURL(input.files[0]);

  const img = document.createElement('img');
  img.src = url;
  img.className = 'image-preview'

  preview.innerHTML = '';
  preview.appendChild(img);
  
})