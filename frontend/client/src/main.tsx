import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import LoginPage from './components/pages/LoginPage.tsx'
import RegisterPage from './components/pages/RegisterPage.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route element={<App />} path='/home'/>
        <Route element={<LoginPage/>} path='/login'/>
        <Route element={<RegisterPage/>} path='/register'/>
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
