import axios from 'axios';

const api = axios.create({
  baseURL: '/api',
});

export const processText = async (text, onProgress) => {
  const response = await api.post('/process', { text }, {
    onUploadProgress: (progressEvent) => {
      const percent = Math.round((progressEvent.loaded * 50) / progressEvent.total);
      onProgress(percent);
    }
  });

  // Simulate remaining progress
  let progress = 50;
  const interval = setInterval(() => {
    progress += Math.random() * 2;
    if (progress >= 100) clearInterval(interval);
    onProgress(Math.min(progress, 100));
  }, 500);

  return response.data;
};

export const uploadDocument = async (file, onProgress) => {
  const formData = new FormData();
  formData.append('file', file);

  const response = await api.post('/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    },
    onUploadProgress: (progressEvent) => {
      const percent = Math.round((progressEvent.loaded * 100) / progressEvent.total);
      onProgress(percent);
    }
  });

  return response.data;
};