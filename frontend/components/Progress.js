export default function Progress({ taskId }) {
    const [progress, setProgress] = useState(0);
  
    useEffect(() => {
      const es = new EventSource(`/api/progress/${taskId}`);
      
      es.onmessage = (event) => {
        const data = JSON.parse(event.data);
        setProgress(data.progress);
        
        if (data.status === 'COMPLETE') {
          es.close();
        }
      };
  
      return () => es.close();
    }, [taskId]);
  
    return (
      <div className="w-full bg-gray-200 rounded-full h-2.5">
        <div 
          className="bg-blue-600 h-2.5 rounded-full" 
          style={{ width: `${progress}%` }}
        ></div>
      </div>
    );
  }