// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'
// JSX is a syntax extension for JavaScript and comes with the full power of JavaScript. You can embed any JavaScript expression in JSX by wrapping it in curly braces.
import { Post } from './Post.jsx'

export function App() {
  // const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <Post
          author="Arthur Gerhardt"
          content="Teste de postagem."
        />
        <Post />
        <Post />
        <Post />
      </div>

      <h1>Hello Vite + React!</h1>
    </>
  )
}

// export default App
