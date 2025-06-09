import {useState, useEffect} from "react";
import {useNavigate} from 'react-router-dom';
import {motion} from "framer-motion";
import Logo from '../assets/static/trophyhunters.png'
import {Snackbar, Alert} from "@mui/material";
import {useUserContext} from "./Context/UserContext.jsx";


function LoginComponent() {
    const navigate = useNavigate()
    const {isLoggedIn, login} = useUserContext()
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
    const [snackbar, setSnackbar] = useState({
        open: false,
        message: "",
        severity: "success",
    });

    const handleUsername = (e) => {
        setUsername(e.target.value)
    }

    const handlePassword = (e) => {
        setPassword(e.target.value)
    }

    useEffect(() => {
        if (isLoggedIn) {
            navigate("/")
        }
    }, []);

    const getProfile = async () => {
        return await fetch('http://api.trophyhunters.tech/profile/me/', {
            headers: { "Authorization": `Bearer ${localStorage.getItem('access')}` },
        }).then(res => res.json())
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        setSnackbar({...snackbar, open: false});
        try {
            const {access, refresh} = await fetch("http://api.trophyhunters.tech/token/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password })
            }).then(res => res.json())

            if (access) {
                localStorage.setItem('access',access)
                localStorage.setItem('refresh',refresh)
                const profile = await getProfile()
                login(profile)
                setSnackbar({open: true, message: "logged successfully", severity: "success"});
                await sleep(1000)
                navigate("/")
            } else {
                setSnackbar({open: true, message: "credentials provided are wrong" || "Error al iniciar sesión", severity: "error"});
            }
        } catch (error) {
            setSnackbar({open: true, message: "Error de red", severity: "error"});
        }
    }

    return (
        <div className="flex flex-col items-center justify-center p-5">
            <motion.img
                src={Logo}
                className="w-72"
                initial={{x: -300, opacity: 0}}
                animate={{x: 0, opacity: 1}}
                transition={{duration: 1}}
            >
            </motion.img>
            <motion.div
                style={{backgroundColor: '#D9D9D920'}}
                className="relative p-8 pt-10 rounded-3xl w-96"
                initial={{x: 300, opacity: 0}}
                animate={{x: 0, opacity: 1}}
                transition={{duration: 1}}
            >
                <form method="POST" onSubmit={handleSubmit} className="mb-5">
                    <div className="flex flex-col gap-6">
                        <div>
                            <input type="text" id="username" className="input-forms" placeholder="Username"
                                   onChange={handleUsername} required="True"/>
                        </div>
                        <div>
                            <input type="password" id="password" className="input-forms" placeholder="Password"
                                   onChange={handlePassword} required="True"/>
                        </div>
                        <div className="flex justify-center">
                            <button type="submit"
                                    className="button">Sign in
                            </button>
                        </div>
                    </div>
                </form>
            </motion.div>
            <Snackbar
                open={snackbar.open}
                autoHideDuration={3000}
                onClose={() => setSnackbar({...snackbar, open: false})}
                anchorOrigin={{vertical: "top", horizontal: "center"}}
            >
                <Alert severity={snackbar.severity} variant="filled" sx={{width: "100%"}}>
                    {snackbar.message}
                </Alert>
            </Snackbar>
        </div>
    )
}

export default LoginComponent