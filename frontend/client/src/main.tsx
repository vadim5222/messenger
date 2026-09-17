import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import LoginPage from './components/LoginPage.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route element={<App />} path='/'/>
        <Route element={<LoginPage/>} path='/login'/>
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
