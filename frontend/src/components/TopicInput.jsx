export default function TopicInput({ topic, setTopic, onSubmit, darkMode }) {
  return (
    <div className="space-y-4">
      <textarea
        className={`w-full p-4 border-2 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-200 resize-none font-sans ${
          darkMode 
            ? 'bg-primary-700 border-primary-600 text-white placeholder-primary-400' 
            : 'bg-white border-primary-200 text-primary-900 placeholder-primary-500'
        }`}
        rows={4}
        placeholder="Describe your dataset... (e.g., 'Customer data for an e-commerce platform' or 'Employee records for a tech company')"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />
      <button
        onClick={onSubmit}
        disabled={!topic.trim()}
        className={`w-full px-6 py-3 rounded-xl font-medium transition-all duration-200 flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed ${
          darkMode 
            ? 'bg-gradient-to-r from-primary-500 to-primary-600 hover:from-primary-600 hover:to-primary-700 text-white shadow-lg hover:shadow-xl' 
            : 'bg-gradient-to-r from-primary-500 to-primary-600 hover:from-primary-600 hover:to-primary-700 text-primary-900 shadow-lg hover:shadow-xl'
        }`}
      >
        <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
          <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-8.293l-3-3a1 1 0 00-1.414 1.414L10.586 9.5H7a1 1 0 100 2h3.586l-1.293 1.293a1 1 0 101.414 1.414l3-3a1 1 0 000-1.414z" clipRule="evenodd" />
        </svg>
        Generate Schema
      </button>
    </div>
  );
}
