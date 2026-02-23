export default function TopicInput({ topic, setTopic, onSubmit }) {
  return (
    <div className="mb-6">
      <textarea
        className="w-full p-3 border rounded-lg focus:ring"
        rows={3}
        placeholder="Describe the dataset you want..."
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />
      <button
        onClick={onSubmit}
        className="mt-3 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Generate Schema
      </button>
    </div>
  );
}
