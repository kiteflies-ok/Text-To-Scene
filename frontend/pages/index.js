import { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const response = await axios.post('/api/process', { text });
      setResult(response.data);
    } catch (error) {
      console.error(error);
    }
    setLoading(false);
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Text to Scene Converter</h1>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          className="w-full p-4 border rounded-lg"
          rows="6"
          placeholder="Enter your text here..."
        />
        
        <button
          type="submit"
          disabled={loading}
          className="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 disabled:bg-gray-400"
        >
          {loading ? 'Processing...' : 'Convert to Animation'}
        </button>
      </form>

      {result && (
        <div className="mt-8">
          <video controls src={result.animation} className="w-full rounded-lg" />
          <audio controls src={result.voiceover} className="mt-4" />
          <div className="mt-4 p-4 bg-gray-100 rounded-lg">
            <h3 className="font-bold mb-2">Summary:</h3>
            <p>{result.summary}</p>
          </div>
        </div>
      )}
    </div>
  );
}