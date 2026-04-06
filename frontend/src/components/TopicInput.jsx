export default function TopicInput({ topic, setTopic, onSubmit, darkMode }) {
  return (
    <div className="space-y-4">
      <div>
        <label className={`block text-sm font-semibold mb-2 text-theme theme-transition`}>
          Describe your dataset
        </label>
        <textarea
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          placeholder="e.g., Generate customer data with names, emails, and purchase history..."
          className={`input resize-none h-32 theme-transition ${
            darkMode 
              ? 'bg-primary-800 border-theme-accent2/30 text-theme placeholder-theme-accent2/60' 
              : 'bg-primary-50 border-theme-accent1/30 text-theme placeholder-theme-accent1/60'
          }`}
          rows={4}
        />
      </div>
      <button
        onClick={onSubmit}
        disabled={!topic.trim()}
        className={`btn btn-primary w-full theme-transition ${
          darkMode 
            ? 'bg-gradient-to-r from-theme-accent1 to-theme-accent2 hover:from-theme-accent2 hover:to-theme-hover text-theme shadow-lg hover:shadow-xl' 
            : 'bg-gradient-to-r from-theme-button to-theme-accent2 hover:from-theme-accent1 hover:to-theme-button text-theme shadow-lg hover:shadow-xl'
        }`}
      >
        <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
          <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
        </svg>
        Generate Schema
      </button>
    </div>
  );
}
