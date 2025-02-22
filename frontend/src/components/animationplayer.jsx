import { useState } from 'react';
import ReactPlayer from 'react-player';

export default function AnimationPlayer({ animationUrl, voiceoverUrl, summary }) {
  const [playing, setPlaying] = useState(false);
 
  return (
    <div className="bg-gray-900 rounded-xl overflow-hidden shadow-xl">
      <div className="relative aspect-video bg-black">
        <ReactPlayer
          url={animationUrl}
          playing={playing}
          controls
          width="100%"
          height="100%"
          config={{
            file: {
              attributes: {
                crossOrigin: 'anonymous'
              }
            }
          }}
        />
      </div>

      <div className="p-6">
        <div className="flex items-center gap-4 mb-4">
          <audio
            src={voiceoverUrl}
            controls
            className="flex-1"
            onPlay={() => setPlaying(true)}
            onPause={() => setPlaying(false)}
          />
        </div>

        <div className="bg-gray-800 rounded-lg p-4">
          <h3 className="font-semibold text-white mb-2">Content Summary</h3>
          <p className="text-gray-300 leading-relaxed">{summary}</p>
        </div>

        <div className="mt-4 grid grid-cols-2 gap-4">
          <button className="bg-gray-700 text-white px-4 py-2 rounded-lg hover:bg-gray-600 transition">
            Download Animation
          </button>
          <button className="bg-gray-700 text-white px-4 py-2 rounded-lg hover:bg-gray-600 transition">
            Share Result
          </button>
        </div>
      </div>
    </div>
  );
}