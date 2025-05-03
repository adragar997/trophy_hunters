import LoginComponent from "./components/LoginComponent.jsx";
import NavComponent from "./components/NavComponent.jsx";
import './App.css'
import {Route, Routes} from "react-router-dom";
import RegisterComponent from "./components/RegisterComponent.jsx";

function App() {
  return (
    <div>
        <NavComponent />
        <Routes>
            <Route path="trophyhunters/register" element={<RegisterComponent/>}/>
            <Route path="trophyhunters/login" element={<LoginComponent/>}/>
        </Routes>
    </div>
  )
}

export default App
