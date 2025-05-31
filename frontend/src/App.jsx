import LoginComponent from "./components/LoginComponent.jsx";
import NavComponent from "./components/NavComponent.jsx";
import './App.css'
import {Route, Routes} from "react-router-dom";
import RegisterComponent from "./components/RegisterComponent.jsx";
import {useState} from "react";
import GamesComponent from "./components/GamesComponent.jsx";
import HomeComponent from "./components/HomeComponent.jsx";

function App() {
    const [user, setUser] = useState()

  return (
    <div>
        <NavComponent user={user} />
        <Routes>
            <Route path="/register" element={<RegisterComponent/>}/>
            <Route path="/games" element={<GamesComponent/>}/>
            <Route path="/home" element={<HomeComponent/>}/>
            <Route path="/login" element={<LoginComponent setUser={setUser}/>}/>
        </Routes>
    </div>
  )
}

export default App
