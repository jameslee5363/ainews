import { useEffect, useState } from "react"
import { Link } from "react-router-dom"

function Home() {
  const [stories, setStories] = useState([])

  useEffect(() => {
    fetch("/summaries.json")
      .then(res => res.json())
      .then(data => setStories(data))
      .catch(err => console.error("Failed to load summaries", err))
  }, [])

  if (!stories.length) return <p className="p-4">Loading summaries...</p>

  return (
    <div className="p-4 space-y-4 max-w-3xl mx-auto">
      {stories.map(story => (
        <Link
          to={`/story/${story.id}`}
          key={story.id}
          className="block border rounded p-4 hover:bg-gray-50"
        >
          <h2 className="text-xl font-semibold mb-1">{story.title}</h2>
          <p className="text-sm text-gray-600">
            {story.summary.slice(0, 160)}...
          </p>
        </Link>
      ))}
    </div>
  )
}

export default Home
