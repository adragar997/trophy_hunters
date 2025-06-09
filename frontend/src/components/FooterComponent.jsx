import {useState} from "react";
import {Link} from "react-router-dom";
import Instragram from "../assets/static/instragram.png"
import Twitter from "../assets/static/twitter.png"
import Facebook from "../assets/static/facebook.png"
import Tiktok from "../assets/static/tiktok.png"
import Email from "../assets/static/email.png"

export default function FooterComponent() {
    const [openIndex, setOpenIndex] = useState(null);

    const toggle = (index) => {
        setOpenIndex(openIndex === index ? null : index);
    };

    const sections = [
        {
            title: 'Nav',
            content: (
                <>
                    <Link to="/">Home</Link>
                    <Link to="/games">Games</Link>
                    <Link to="/news">News</Link>
                    <Link to="/FAQ">FAQ</Link>
                </>
            ),
        },
        {
            title: 'Legal',
            content: (
                <>
                    <span>Privacy policy</span>
                    <span>Cookie policy</span>
                    <span>Legal notice</span>
                    <span>Terms & conditions</span>
                </>
            ),
        },
        {
            title: 'FAQ',
            content: (
                <>
                    <Link to="/FAQ">Users</Link>
                    <Link to="/FAQ">Games</Link>
                    <Link to="/FAQ">Cookies</Link>
                </>
            ),
        },
        {
            title: 'Account',
            content: (
                <>
                    <Link to="/profile">Profile</Link>
                    <Link to="/settings">Settings</Link>
                </>
            ),
        },
        {
            title: 'Contact us',
            content: (
                <>
                    <div className="flex gap-2 mb-2">
                        <img src={Instragram} alt="Instragram" className="w-6"/>
                        <img src={Facebook} alt="Facebook" className="w-6"/>
                        <img src={Tiktok} alt="Tiktok" className="w-6"/>
                        <img src={Twitter} alt="Twitter" className="w-6"/>
                    </div>
                    <div className="flex items-center gap-2">
                        <img src={Email} alt="Email" className="w-6"/>
                        <span>trophyhunters@gmail.com</span>
                    </div>
                </>
            ),
        },
    ];

    return (
        <footer
            style={{backgroundColor: '#D9D9D920'}}
            className="w-full text-white/50 p-5 font-open"
        >
            <div className="lg:hidden flex flex-col gap-4">
                {sections.map((section, i) => (
                    <div key={i} className="border-b border-white/10 pb-2">
                        <button
                            onClick={() => toggle(i)}
                            className="w-full text-left font-bold text-[20px] flex justify-between items-center"
                        >
                            {section.title}
                            <span className={`transition-transform ${openIndex === i ? 'rotate-180' : ''}`}>⌄</span>
                        </button>
                        {openIndex === i && (
                            <div className="mt-2 flex flex-col gap-1 text-sm pl-2">
                                {section.content}
                            </div>
                        )}
                    </div>
                ))}
            </div>

            <div className="hidden lg:grid grid-cols-5 gap-6">
                {sections.map((section, i) => (
                    <div key={i} className="flex flex-col gap-2">
                        <h3 className="font-bold text-[25px]">{section.title}</h3>
                        <div className="flex flex-col gap-1 text-sm">{section.content}</div>
                    </div>
                ))}
            </div>

            <div className="mt-1 text-center text-xs text-white/30">
                <span>© trophyhunters.tech</span>
            </div>
        </footer>
    )
}