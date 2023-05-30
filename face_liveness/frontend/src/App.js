import React from 'react';
import './App.css';
import { FaceLivenessDetector } from '@aws-amplify/ui-react-liveness';
import { Loader, ThemeProvider } from '@aws-amplify/ui-react';

import { Amplify } from 'aws-amplify';
import '@aws-amplify/ui-react/styles.css';
import awsexports from './aws-exports';

Amplify.configure(awsexports);


function App() {
  const [loading, setLoading] = React.useState(true);
  const [createLivenessApiData, setCreateLivenessApiData] = React.useState(null);

  React.useEffect(() => {
    const fetchCreateLiveness = async () => {
     
      // appel à notre API : on récupère le session id
      const response  = await fetch('http://localhost:4242/getsessionid');
      const data      = await response.json();
      console.log(data);
      setCreateLivenessApiData(data);
      setLoading(false);
    };

    fetchCreateLiveness();
  }, []);

  const handleAnalysisComplete = async () => {
    /*
     * TODO
     */
    const response = await fetch(
      `/api/get?sessionId=${createLivenessApiData.sessionId}`
    );
    const data = await response.json();

    /*
     * Note: The isLive flag is not returned from the GetFaceLivenessSession API
     * This should be returned from your backend based on the score that you
     * get in response. Based on the return value of your API you can determine what to render next.
     * Any next steps from an authorization perspective should happen in your backend and you should not rely
     * on this value for any auth related decisions.
     */
    if (data.isLive) {
      console.log('User is live');
    } else {
      console.log('User is not live');
    }
  };

  return (
    <div className='detector'>
    <ThemeProvider> {loading ? (<Loader className='loader' /> ) : (
        <FaceLivenessDetector   className="detector"
          sessionId={createLivenessApiData.sessionId}
          region="eu-west-1"
          onAnalysisComplete={handleAnalysisComplete}
        />
      )}
    </ThemeProvider>
    </div>
  );
}

export default App;
