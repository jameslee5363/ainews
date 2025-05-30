import { useEffect, useState } from "react"
import { useParams, Link } from "react-router-dom"

function Story() {
  const { id } = useParams()
  const [story, setStory] = useState(null)

  useEffect(() => {
    fetch("/summaries.json")
      .then(res => res.json())
      .then(data => {
        const found = data.find(item => item.id === id)
        setStory(found)
      })
      .catch(err => console.error("Failed to load story", err))
  }, [id])

  if (!story) return <p className="p-4">Loading story...</p>

  return (
    <div className="p-6 max-w-3xl mx-auto space-y-6">
      <Link to="/" className="text-blue-600">&larr; Back</Link>

      <h1 className="text-2xl font-bold">{story.title}</h1>

      <article className="prose">
        <p>{story.summary}</p>
      </article>

      <hr />

      <h2 className="text-xl font-semibold">Original articles</h2>
      {story.sources.map((src, i) => (
        <div key={i} className="border rounded p-3 my-3">
          <p className="text-sm font-semibold mb-1">{src.source}</p>
          <p className="text-sm mb-2">
            <a href={src.url} target="_blank" rel="noopener noreferrer" className="text-blue-600">
              Read full article
            </a>
          </p>
          <p className="text-sm text-gray-700 whitespace-pre-line">
            {src.content.slice(0, 600)}...
          </p>
        </div>
      ))}
    </div>
  )
}

export default Story
