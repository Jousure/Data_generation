import { generateCSV } from "../api/backend";

export default function GenerateButton({ columns, rows }) {
  async function handle() {
    const res = await generateCSV(columns, rows);
    alert(`CSV generated: ${res.file}`);
  }

  return (
    <button
      onClick={handle}
      className="px-5 py-2 bg-purple-600 text-white rounded hover:bg-purple-700"
    >
      Download CSV
    </button>
  );
}
