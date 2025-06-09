import {useState} from "react";
import Logo from "../assets/static/trophyhunters.png";
import {motion} from "framer-motion";
import {Alert, Snackbar} from "@mui/material";
import {useNavigate} from "react-router-dom";

function RegisterComponent() {
    const [formData, setFormData] = useState(
            {
            'username': '',
            'password':'',
            'avatar':null,
            'banner':null,
            'bio': '',
            'firstname': '',
            'lastname': '',
            'birthdate': ''
        }
    )
    const navigate = useNavigate()
    const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
    const [snackbar, setSnackbar] = useState({
        open: false,
        message: "",
        severity: "success", // 'success' | 'error'
    });

    const handleSubmit = async (e) => {
        e.preventDefault()
        const payload = new FormData();

        payload.append("username",  formData.username);
        payload.append("password",  formData.password);
        if (formData.avatar) payload.append("avatar", formData.avatar);
        if (formData.banner) payload.append("banner", formData.banner);
        payload.append("bio",       formData.bio);
        payload.append("firstname", formData.firstname);
        payload.append("lastname",  formData.lastname);
        payload.append("birthdate", formData.birthdate);

        const response = await fetch('http://127.0.0.1:8000/register/',{
            method: "POST",
            body: payload,
        })

        if (response.status === 200) {
            setSnackbar({open: true, message: "Signed up successfully", severity: "success"});
            await sleep(1000)
            navigate("/login")
        } else {
            setSnackbar({open: true, message: "Something went wrong", severity: "error"});
        }
    }

    const handleChange = (e) => {
        const {id, value} = e.target
        setFormData(prev => ({...prev, [id]:value}))
    }

    const handleImage = (e) => {
        const {id, files} = e.target
        setFormData(prev => ({ ...prev, [id]: files[0] }));
    }

    return (
        <div className="flex flex-col items-center justify-center min-h-screen">
            <motion.img
                src={Logo}
                className="w-72"
                initial={{y: -300, opacity: 0}}
                animate={{y: 0, opacity: 1}}
                transition={{duration: 1}}
            >
            </motion.img>
            <motion.div
                style={{backgroundColor: '#D9D9D920'}}
                className="relative p-8 pt-10 rounded-3xl w-96"
                initial={{y: 300, opacity: 0}}
                animate={{y: 0, opacity: 1}}
                transition={{duration: 1}}
            >
                <form method="post" onSubmit={handleSubmit}>
                    <div className="flex flex-col gap-5">
                        <div className="flex gap-3">
                            <input type="text" id="username" name="username" placeholder="Username"
                                   className="input-forms"
                                   required="True" onChange={handleChange}/>

                            <input type="password" id="password" name="password" placeholder="Password"
                                   required="True" className="input-forms" onChange={handleChange}/>
                        </div>
                        <div className="flex gap-3">
                            <input type="text" id="firstname" name="firstname" className="input-forms"
                                   placeholder="First Name" onChange={handleChange}/>

                            <input type="text" id="lastname" name="lastname" className="input-forms"
                                   placeholder="Last Name" onChange={handleChange}/>
                        </div>

                        <div className="flex gap-3">
                            <input type="file" id="avatar" name="avatar" className="file:bg-gradient-to-r file:from-cyan-500 file:to-teal-500 file:text-black file:font-semibold file:py-2 file:px-4 file:rounded-full file:border-0 file:cursor-pointer
             w-[500px] min-w-[120px] overflow-hidden file:w-full"
                                   onChange={handleImage}/>

                            <input type="file" id="banner" name="banner" className="file:bg-gradient-to-r file:from-cyan-500 file:to-teal-500 file:text-black file:font-semibold file:py-2 file:px-4 file:rounded-full file:border-0 file:cursor-pointer
             w-[500px] min-w-[120px] overflow-hidden file:w-full"
                                   onChange={handleImage}/>
                        </div>

                        <input type="date" id="birthdate" name="birthdate" className="input-forms"
                               placeholder="Birthday" onChange={handleChange}/>

                        <textarea id="bio" cols="20" rows="5" name="bio" className="input-forms"
                                  placeholder="About me" onChange={handleChange}></textarea>

                        <div className="flex justify-center pb-2">
                            <button type="submit"
                                    className="button">Sign up
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

export default RegisterComponent