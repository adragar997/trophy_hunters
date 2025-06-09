import { useState } from "react";
import {Link} from "react-router-dom";

export default function FaqComponent() {
const faqs = {
  Users: [
    {
      question: "How can i create an account?",
      answer: (
          <>
            Yes, You can sign up from <Link to="/register"><span className="underline">here</span></Link>.
            </>
      )
    },
    {
      question: "Can i delete my account?",
      answer: "Not yet, but we will implement it as soon as possible"
    }
  ],
  Games: [
    {
      question: "Can i add my own games?",
      answer: "No, you can't because we fetch every game that player has automatically and we adde to our DB, that's why you could see every day new games and new changes"
    }
  ],
  Cookies: [
    {
      question: "Do you use cookies?",
      answer: "Not yet, we are thinking in doing it soon"
    }
  ]
};

  const [openIndex, setOpenIndex] = useState({});

  const toggle = (section, index) => {
    setOpenIndex((prev) => ({
      ...prev,
      [section]: prev[section] === index ? null : index
    }));
  };

  return (
    <div className="text-white px-6 py-10 max-w-3xl mx-auto font-open space-y-10">
      {Object.entries(faqs).map(([section, questions]) => (
        <div key={section}>
          <h1 className="text-[35px] mb-2 border-b-2 border-orange-400  w-fit pb-1"
          >
            {section}
          </h1>

          {questions.map((item, idx) => (
            <div key={idx} className="bg-[#2a2a2a] mb-2">
              <button
                onClick={() => toggle(section, idx)}
                className="w-full text-left text-[25px] p-4 flex justify-between items-center"
              >
                <span>{item.question}</span>
                <span>{openIndex[section] === idx ? "-" : "+"}</span>
              </button>
              {openIndex[section] === idx && (
                <div className="bg-[#1e1e1e] px-6 py-3 text-[20px] text-gray-300">
                  {item.answer}
                </div>
              )}
            </div>
          ))}
        </div>
      ))}
    </div>
  );
}