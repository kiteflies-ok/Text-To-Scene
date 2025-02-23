export default function Loader({ progress }) {
    return (
      <div className="relative w-full h-2 bg-gray-700 rounded-full overflow-hidden">
        <div
          className="absolute left-0 top-0 h-full bg-blue-500 transition-all duration-300 ease-out"
          style={{ width: `${progress}%` }}
        >
          <div className="absolute right-0 inset-y-0 w-2 bg-blue-400 animate-pulse" />
        </div>
      </div>
    );
  }