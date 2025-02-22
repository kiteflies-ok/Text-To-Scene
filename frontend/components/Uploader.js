import { useCallback } from 'react';

export default function Uploader({ onUpload }) {
  const handleFile = useCallback(async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await axios.post('/api/upload', formData, {
      onUploadProgress: progress => {
        const percent = Math.round((progress.loaded * 100) / progress.total);
        setProgress(percent);
      }
    });
    
    onUpload(response.data.file_id);
  }, []);

  return (
    <div className="border-dashed border-2 p-8 text-center">
      <input 
        type="file" 
        onChange={(e) => handleFile(e.target.files[0])}
        accept=".pdf,.docx,.txt"
      />
      <p>Drag and drop documents or click to upload</p>
    </div>
  );
}