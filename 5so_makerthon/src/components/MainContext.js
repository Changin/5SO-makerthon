import React from 'react';
import styled  from 'styled-components';
import VideoPlay from './VideoPlay';
import "./styles/MainContext.css";
import "../App.css"

const MainContextBlock = styled.div`
margin-top:15px;
  h1 {
    font-family: "strongmil_bold";
    margin: 0;
    font-size: 50px;
    color: white;
  }
`;



function MainContext() {
    return (
      <>
      <div class="centered">
          <MainContextBlock>
              <h1>거수자 속에 포상 휴가있다!</h1>
          </MainContextBlock>
        </div>
        <div class="channel">
          <h4>&#91;CH1&#93;</h4>
        </div>
        <VideoPlay />
    </>
    )  
      }

export default MainContext;