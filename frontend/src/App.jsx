import { useState } from "react";
import TopicInput from "./components/TopicInput";
import ColumnEditor from "./components/ColumnEditor";
import PreviewTable from "./components/PreviewTable";
import GenerateButton from "./components/GenerateButton";
import RowSelector from "./components/RowSelector";
import { getSchema, getPreview } from "./api/backend";

export default function App() {
  const [topic, setTopic] = useState("");
  const [columns, setColumns] = useState([]);
  const [rows, setRows] = useState(100);
  const [preview, setPreview] = useState([]);

  async function handleSchema() {
    const res = await getSchema(topic);
    setColumns(res.columns);
  }

  async function handlePreview() {
    const res = await getPreview(columns);
    setPreview(res.preview);
  }

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-4xl mx-auto bg-white p-6 rounded shadow">
        <h1 className="text-3xl font-bold mb-6">Dataset Generator</h1>

        <TopicInput topic={topic} setTopic={setTopic} onSubmit={handleSchema} />

        {columns.length > 0 && (
          <>
            <ColumnEditor columns={columns} setColumns={setColumns} />
            <button
              onClick={handlePreview}
              className="mb-6 px-4 py-2 bg-gray-800 text-white rounded"
            >
              Preview Data
            </button>
          </>
        )}

        <PreviewTable data={preview} />

        <RowSelector rows={rows} setRows={setRows} />

        {preview.length > 0 && <GenerateButton columns={columns} rows={rows} />}
      </div>
    </div>
  );
}
