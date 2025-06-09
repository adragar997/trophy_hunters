import {createContext, useState, useContext} from "react";
import {useNavigate} from "react-router-dom";

const userContext = createContext();

export const UserProvider = ({children}) => {
    const navigate = useNavigate()

    const [profile, setProfile] = useState(() => {
        const stored = localStorage.getItem("profile")
        return stored ? JSON.parse(stored) : null
    });
    const [isLoggedIn, setIsLoggedIn] = useState(() => localStorage.getItem('isLoggedIn') || false);

    const login = (info) => {
        setProfile(info)
        setIsLoggedIn(true);
        localStorage.setItem("profile", JSON.stringify(info));
        localStorage.setItem("isLoggedIn", "true");
    };

    const logout = () => {
        setProfile({})
        setIsLoggedIn(false)
        localStorage.removeItem("profile");
        localStorage.removeItem("isLoggedIn");
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
        navigate("/")
    };

    return (
        <userContext.Provider value={{profile,login, isLoggedIn,logout}}>
            {children}
        </userContext.Provider>
    );
};

export const useUserContext = () => useContext(userContext);