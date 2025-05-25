import {Link} from "react-router-dom";
import '../assets/css/Navbar.css'

function NavComponent(props) {
    const {user} = props
    return (
        <header>
          <nav>
              <div className="flex justify-between">
                {user ?
                    <div>
                        Bienvenido {user.username}
                    </div>
                    :
                    <div>
                        <Link to="/register">Registro</Link>
                        <Link to="/login">Login</Link>
                    </div>
                }
                  <input type="text" placeholder="buscar "/>
              </div>
          </nav>
        </header>
    )
}


export default NavComponent