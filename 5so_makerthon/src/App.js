import React from "react";
import "./App.css";
import {createGlobalStyle} from 'styled-components';
import MainContext from "./components/MainContext.js";

const GlobalStyle=createGlobalStyle`
body{
  background:#536349;

  p {
    font-family:"NanumSquareRoundL";
    font-size:11px;
    float:right;
    margin-bottom:0px;
  }
}
`;

function App() {

 
  return(
    <>
    <GlobalStyle />
    <div><MainContext /></div>


    <p>Copyright (c) 2021 이승엽,
      김창현, 이준용, 한준서, 백창인</p>
    </>
  )
}

export default App;
