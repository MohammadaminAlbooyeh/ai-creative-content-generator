const LOG_LEVELS = { debug: 0, info: 1, warn: 2, error: 3 };
const CURRENT_LEVEL = LOG_LEVELS[process.env.REACT_APP_LOG_LEVEL] || LOG_LEVELS.info;

const formatLog = (level, message, data) => {
  const entry = {
    timestamp: new Date().toISOString(),
    level,
    message,
    ...(data ? { data } : {}),
  };
  if (process.env.NODE_ENV === 'development') {
    const fn = level === 'error' ? 'error' : level === 'warn' ? 'warn' : 'log';
    console[fn](`[${level.toUpperCase()}] ${message}`, data || '');
  }
  return entry;
};

const logger = {
  debug: (msg, data) => {
    if (CURRENT_LEVEL <= LOG_LEVELS.debug) formatLog('debug', msg, data);
  },
  info: (msg, data) => {
    if (CURRENT_LEVEL <= LOG_LEVELS.info) formatLog('info', msg, data);
  },
  warn: (msg, data) => {
    if (CURRENT_LEVEL <= LOG_LEVELS.warn) formatLog('warn', msg, data);
  },
  error: (msg, data) => {
    if (CURRENT_LEVEL <= LOG_LEVELS.error) formatLog('error', msg, data);
  },
};

export default logger;
