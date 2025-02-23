import { useState } from 'react';
import { processText, uploadDocument } from '../utils/api';
import FileUploader from '../components/fileuploader';
import AnimationPlayer from '../components/AnimationPlayer';
import Loader from '../components/Loader';

export default function Home() {
  const [inputText, setInputText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [progress, setProgress] = useState(0);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputText) return;
   
    try {
      setLoading(true);
      setError(null);
      const response = await processText(inputText, setProgress);
      setResult(response);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleFileUpload = async (file) => {
    try {
      setLoading(true);
      setError(null);
      const response = await uploadDocument(file, setProgress);
      setResult(response);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 to-gray-800">
      <Navbar />
     
      <main className="container mx-auto px-4 py-12">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-4xl font-bold text-center text-white mb-8">
            Transform Text into Engaging Animations
          </h1>

          <div className="bg-gray-800 rounded-2xl p-6 shadow-xl">
            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="flex gap-4">
                <textarea
                  value={inputText}
                  onChange={(e) => setInputText(e.target.value)}
                  placeholder="Paste your text or document content here..."
                  className="flex-1 bg-gray-700 text-white rounded-xl p-4 min-h-[200px]
                            focus:ring-2 focus:ring-blue-500 focus:outline-none"
                />
               
                <div className="w-px bg-gray-600" />
               
                <FileUploader
                  onFileUpload={handleFileUpload}
                  className="flex-1"
                />
              </div>

              <button
                type="submit"
                disabled={loading || (!inputText && !result?.text)}
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold
                          py-4 px-8 rounded-xl transition-all duration-200 disabled:opacity-50"
              >
                {loading ? 'Creating Magic...' : 'Generate Animation'}
              </button>
            </form>

            {loading && (
              <div className="mt-6">
                <Loader progress={progress} />
                <p className="text-center text-gray-400 mt-4">
                  {progress < 50 ? 'Analyzing content...' :
                   progress < 80 ? 'Rendering animation...' :
                   'Adding final touches...'}
                </p>
              </div>
            )}

            {error && (
              <div className="mt-6 p-4 bg-red-100 text-red-700 rounded-lg">
                {error}
              </div>
            )}

            {result && (
              <div className="mt-8 animate-fade-in">
                <AnimationPlayer
                  animationUrl={result.animation}
                  voiceoverUrl={result.voiceover}
                  summary={result.summary}
                />
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}