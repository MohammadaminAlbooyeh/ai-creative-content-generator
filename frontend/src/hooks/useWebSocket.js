import { useEffect, useRef, useState } from 'react';

export function useWebSocket(url) {
  const [isConnected, setIsConnected] = useState(false);
  const [messages, setMessages] = useState([]);
  const ws = useRef(null);

  useEffect(() => {
    ws.current = new WebSocket(url);
    ws.current.onopen = () => setIsConnected(true);
    ws.current.onmessage = (event) => {
      setMessages((prev) => [...prev, event.data]);
    };
    ws.current.onclose = () => setIsConnected(false);
    return () => ws.current?.close();
  }, [url]);

  const send = (data) => {
    ws.current?.send(JSON.stringify(data));
  };

  return { isConnected, messages, send };
}
