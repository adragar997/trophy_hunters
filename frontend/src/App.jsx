import LoginComponent from "./components/LoginComponent.jsx";
import NavComponent from "./components/NavComponent.jsx";
import {Route, Routes} from "react-router-dom";
import RegisterComponent from "./components/RegisterComponent.jsx";
import GamesComponent from "./components/GamesComponent.jsx";
import FooterComponent from "./components/FooterComponent.jsx";
import HomeComponent from "./components/HomeComponent.jsx";
import GameDetails from "./components/GameDetailsComponent.jsx";
import FaqComponent from "./components/FaqComponent.jsx";
import BackgroundPage from "./assets/static/backgroundPage.png"
import './App.css'
import NewsComponent from "./components/NewsComponent.jsx.jsx";
import SettingsComponent from "./components/SettingsComponent.jsx";
import ProfileComponent from "./components/ProfileComponent.jsx";

function App() {

    return (
        <div className="min-h-screen flex flex-col" style={{
            backgroundImage: `url(${BackgroundPage})`,
            backgroundSize: 'cover',
            backgroundRepeat: 'no-repeat',
            backgroundPosition: 'center',
            backgroundAttachment: 'fixed',
            minHeight: '100vh'
        }}>
            <NavComponent/>
            <main className="flex-1">
                <Routes>
                    <Route path="/register" element={<RegisterComponent/>}/>
                    <Route path="/games" element={<GamesComponent/>}/>
                    <Route path="/settings" element={<SettingsComponent/>}/>
                    <Route path="/profile" element={<ProfileComponent/>}/>
                    <Route path="/news" element={<NewsComponent/>}/>
                    <Route path="/games/:id" element={<GameDetails/>}/>
                    <Route path="/FAQ" element={<FaqComponent/>}/>
                    <Route path="/" element={<HomeComponent/>}/>
                    <Route path="/login" element={<LoginComponent/>}/>
                </Routes>
            </main>
            <FooterComponent/>
        </div>
    )
}

export default App
