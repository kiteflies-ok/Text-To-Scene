import { useCallback } from 'react';

export default function FileUploader({ onFileUpload, className }) {
  const handleFile = useCallback(async (file) => {
    if (!file) return;
    if (!['application/pdf', 'text/plain', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'].includes(file.type)) {
      throw new Error('Unsupported file format');
    }
    await onFileUpload(file);
  }, [onFileUpload]);

  return (
    <div className={`border-2 border-dashed border-gray-600 rounded-xl p-8 text-center ${className}`}>
      <input
        type="file"
        onChange={(e) => handleFile(e.target.files[0])}
        className="hidden"
        id="file-upload"
        accept=".pdf,.docx,.txt"
      />
      <label
        htmlFor="file-upload"
        className="cursor-pointer flex flex-col items-center text-gray-400"
      >
        <svg className="w-16 h-16 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
        </svg>
        <p className="text-lg">
          Drag & drop files or <span className="text-blue-500">browse</span>
        </p>
        <p className="text-sm mt-2">Supported formats: PDF, DOCX, TXT</p>
      </label>
    </div>
  );
}