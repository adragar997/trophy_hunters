import {Link} from "react-router-dom";
import '../assets/css/Navbar.css'

function NavComponent(props) {
    const {user} = props
    return (
        <header>
          <nav>
              <div className="flex justify-center">
                {user ?
                    <div>
                        Bienvenido {user.username}
                    </div>
                    :
                    <div className="justify-between">
                        <Link to="/register">Registro</Link>
                        <Link to="/login">Login</Link>
                    </div>
                }
              </div>
          </nav>
        </header>
    )
}


export default NavComponent