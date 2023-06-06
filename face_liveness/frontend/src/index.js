import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Liveness from "./liveness";
import {Amplify} from "aws-amplify";
import awsexports from "./aws-exports";
import '@aws-amplify/ui-react/styles.css';

Amplify.configure(awsexports);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Liveness>
    </Liveness>
);

