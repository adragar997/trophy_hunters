import { useEffect, useState } from "react";
import { useUserContext } from "./Context/UserContext.jsx";
import UnlockedOverlayIcon from '../assets/static/unlocked.png';
import TrophyIcon from '../assets/static/trophy.png'; // Importa el icono de trofeo
function GameWithTrophies({ game }) {
  const [open, setOpen] = useState(false);
  const hasTrophies = game.game.trophies && game.game.trophies.length > 0;

  return (
    <div className="flex items-start mb-6 text-white relative w-full">
      <div className="relative flex-shrink-0 z-10">
        <img
          src={game.game.cover}
          alt={game.game.name}
          className="w-28 h-40 object-cover rounded-lg cursor-pointer shadow-lg transform transition-transform duration-200 hover:scale-105"
          onClick={() => setOpen(!open)}
        />
        {game.game.trophies && game.game.trophies.length > 0 && (
          <div className="absolute bottom-1 left-1 bg-gradient-to-r from-yellow-600 to-orange-600 text-white text-xs font-bold px-1.5 py-0.5 rounded-full flex items-center shadow-md">
            <img src={TrophyIcon} alt="Número de Trofeos" className="w-4 h-4 mr-1" />
            <span>{game.game.trophies.length}</span>
          </div>
        )}
      </div>

      {open && hasTrophies && (
        <div className="ml-6 flex-grow p-4 rounded-lg shadow-2xl grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4 max-w-[calc(100vw-200px)] overflow-y-auto max-h-[400px] animate-fade-in z-20">
          {game.game.trophies.map((trophy) => (
            <div
              key={trophy.name}
              className={`relative flex flex-col items-center p-3 rounded-lg transition-colors duration-200`}
            >
                <div className="relative mb-2">
                    <img
                        src={trophy.achieved ? trophy.unlocked_icon : trophy.blocked_icon}
                        alt={trophy.name}
                        className="w-20 h-20 object-contain flex-shrink-0 filter drop-shadow-lg"
                    />
                    {trophy.achieved && (
                        <img
                            src={UnlockedOverlayIcon}
                            alt="Trofeo Desbloqueado"
                            className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 w-8 h-8 object-contain drop-shadow-md"
                        />
                    )}
                </div>
              <div className="flex flex-col text-center">
                <span
                  className={`text-base font-semibold ${
                    trophy.achieved ? "text-green-300" : "text-white"
                  }`}
                >
                  {trophy.name}
                </span>
                {trophy.description && (
                  <span className="text-xs text-gray-300 mt-1 line-clamp-2">
                    {trophy.description}
                  </span>
                )}
              </div>
            </div>
          ))}
        </div>
      )}

      {!open && (
        <div className="ml-4 flex flex-col justify-center max-w-[200px] z-10">
          <h3 className="text-xl font-bold text-white truncate drop-shadow-md">
            {game.game.name}
          </h3>
          {!hasTrophies && (
            <p className="text-sm text-gray-300 italic mt-1">Sin trofeos disponibles</p>
          )}
        </div>
      )}
    </div>
  );
}

export default function UserProfile() {
  const { profile, isLoggedIn } = useUserContext();
  const [games, setGames] = useState([]);
  const [recentlyPlayedGames, setRecentlyPlayedGames] = useState([]);

  const fetchData = async () => {
    try {
      const response = await fetch(
        `http://api.trophyhunters.tech/users/${profile?.username}/games/`
      );
      const data = await response.json();
      setGames(data.results);
      setRecentlyPlayedGames(data.results.slice(0, 4)); // Ejemplo
    } catch (error) {
      console.error("Error fetching games:", error);
    }
  };

  useEffect(() => {
    if (profile?.username) {
      fetchData();
    }
  }, [profile]);

  const RecentlyPlayedGameCard = ({ game }) => (
    <div className="flex flex-col items-center group relative cursor-pointer">
      <img
        src={game.game.cover}
        alt={game.game.name}
        className="w-44 h-60 object-cover rounded-lg shadow-xl transition-transform duration-300 group-hover:scale-105"
      />
      <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-black/80 via-black/50 to-transparent p-3 rounded-b-lg opacity-0 group-hover:opacity-100 transition-opacity duration-300">
        <h3 className="text-white text-lg font-semibold text-center truncate">
          {game.game.name}
        </h3>
      </div>
    </div>
  );

  if (!isLoggedIn || !profile) {
    return (
      <div className="min-h-screen flex items-center justify-center text-white text-xl">
        Cargando perfil o no autenticado...
      </div>
    );
  }

  return (
    <div
      className="min-h-screen text-white font-sans"
    >
      <div className="min-h-screen">
        <header className="relative w-full h-60 bg-cover bg-center"
          style={{
            backgroundImage: `url('http://127.0.0.1:8000${profile.profile?.banner}')`,
          }}>
          <div className="absolute inset-0 bg-black opacity-40"></div>
          <div className="relative z-10 flex items-center h-full px-4 sm:px-6 md:px-8">
            <img
              src={`http://127.0.0.1:8000${profile.profile?.avatar}`}
              alt="Avatar"
              className="w-24 h-24 sm:w-28 sm:h-28 md:w-32 md:h-32 rounded-full border-4 border-yellow-400 shadow-xl object-cover flex-shrink-0"
            />
            <h1 className="text-white text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-extrabold ml-2 sm:ml-4 md:ml-6 lg:ml-8 drop-shadow-2xl truncate">
              {profile.username}
            </h1>
          </div>
        </header>

        <main className="max-w-7xl mx-auto p-8 pt-12">
          <section className="mb-16 p-6 rounded-lg">
            <h2 className="text-3xl font-bold text-white mb-8 border-b-2 border-yellow-500 pb-3 drop-shadow-lg">
              Jugados recientemente:
            </h2>
            {recentlyPlayedGames.length > 0 ? (
              <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8 justify-items-center">
                {recentlyPlayedGames.map((game) => (
                  <RecentlyPlayedGameCard key={game.game.id} game={game} />
                ))}
              </div>
            ) : (
              <p className="text-gray-200 italic text-lg">No hay juegos recientes para mostrar.</p>
            )}
          </section>

          <section className="p-6 rounded-lg">
            <h2 className="text-3xl font-bold text-white mb-8 border-b-2 border-yellow-500 pb-3 drop-shadow-lg">
              Mis juegos:
            </h2>
            <div className="flex flex-col items-start space-y-8">
              {games.length > 0 ? (
                games.map((game) => (
                  <GameWithTrophies key={game.game.id} game={game} />
                ))
              ) : (
                <p className="text-gray-200 italic text-lg">No hay juegos en tu colección.</p>
              )}
            </div>
          </section>
        </main>
      </div>

      <style jsx>{`
        @keyframes slide-in {
          from {
            opacity: 0;
            transform: translateX(20px);
          }
          to {
            opacity: 1;
            transform: translateX(0);
          }
        }
        @keyframes fade-in {
          from {
            opacity: 0;
          }
          to {
            opacity: 1;
          }
        }
        .animate-slide-in {
          animation: slide-in 0.3s ease-out forwards;
        }
        .animate-fade-in {
          animation: fade-in 0.3s ease-out forwards;
        }
      `}</style>
    </div>
  );
}