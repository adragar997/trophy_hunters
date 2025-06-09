import {useState, useEffect} from "react";
import {useUserContext} from "./Context/UserContext.jsx";
import {Alert, Grid, Snackbar} from "@mui/material";
import {useNavigate} from "react-router-dom";
import DefaultAvatar from "../assets/static/defaultAvatar.png"

export default function SettingsComponent() {
    const {profile, isLoggedIn} = useUserContext()
    const navigate = useNavigate()
    const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
    const [snackbar, setSnackbar] = useState({
        open: false,
        message: "",
        severity: "success", // 'success' | 'error'
    });
    const [formData, setFormData] = useState(
        {
            'username':"",
            'avatar': null,
            'banner': null,
            'bio': '',
            'birthdate': ''
        }
    )

    const handleSubmit = async (e) => {
        e.preventDefault()
        const payload = new FormData();
        payload.append("username", profile.username )
        if (formData.avatar) payload.append("avatar", formData.avatar);
        if (formData.banner) payload.append("banner", formData.banner);
        payload.append("bio", formData.bio);
        payload.append("birthdate", formData.birthdate);

        const response = await fetch('http://127.0.0.1:8000/update/', {
            method: "PATCH",
            headers: {
                "Authorization": `Bearer ${localStorage.getItem('access')}`
            },
            body: payload,
        })

        if (response.status === 200) {
            navigate("/")
        }
    }

    const handleChange = (e) => {
        const {id, value} = e.target
        setFormData(prev => ({...prev, [id]: value}))
    }

    const handleImage = (e) => {
        const {id, files} = e.target
        setFormData(prev => ({...prev, [id]: files[0]}));
    }

    useEffect(() => {
        const checkLogin = async () => {
            if (!isLoggedIn) {
                navigate("/login");
            }
        };
        checkLogin();
    }, [isLoggedIn]);

    if (!isLoggedIn) return null;

    return (
        <Grid container className="flex justify-center items-center font-open tracking-widest">
            <div className="w-96 p-5 m-10 rounded-2xl flex flex-col gap-5 text-white relative"
                 style={{backgroundColor: '#D9D9D920'}}>
                <div className="flex flex-row gap-7">
                    <div>
                        <img src={profile?.profile.avatar
                            ? `http://127.0.0.1:8000${profile.profile.avatar}`
                            : DefaultAvatar} alt="avatar"
                             className="w-25 h-25 rounded-[50%]"/>
                    </div>
                    <div className="min-h-full flex items-center">
                        <h1 className="text-[22px] font-bold">{profile.username}</h1>
                    </div>
                </div>
                <div>
                    <form method="post" onSubmit={handleSubmit}>
                        <div className="flex flex-col gap-5">
                            <div className="flex gap-3 justify-between">
                                <label htmlFor="avatar" className="">Avatar</label>
                                <label htmlFor="banner">Banner</label>
                            </div>

                            <div className="flex gap-3">
                                <input type="file" id="avatar" name="avatar" className="file:bg-gradient-to-r file:from-cyan-500 file:to-teal-500 file:text-black file:font-semibold file:py-2 file:px-4 file:rounded-full file:border-0 file:cursor-pointer
             w-[500px] min-w-[120px] overflow-hidden file:w-full"
                                       onChange={handleImage}/>

                                <input type="file" id="banner" name="banner" className="file:bg-gradient-to-r file:from-cyan-500 file:to-teal-500 file:text-black file:font-semibold file:py-2 file:px-4 file:rounded-full file:border-0 file:cursor-pointer
             w-[500px] min-w-[120px] overflow-hidden file:w-full"
                                       onChange={handleImage}/>
                            </div>
                            <div className="flex justify-center pb-2">
                                <button type="submit"
                                        className="button">Update profile
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
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
        </Grid>
    )
}