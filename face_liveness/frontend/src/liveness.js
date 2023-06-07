import React from 'react';
import { FaceLivenessDetector } from '@aws-amplify/ui-react-liveness';
import { Loader, ThemeProvider } from '@aws-amplify/ui-react';

export default function Liveness() {
  const [loading, setLoading] = React.useState(true);
  const [createLivenessApiData, setCreateLivenessApiData] = React.useState(null);

  React.useEffect(() => {
    console.log('fetching create liveness api data')
    const fetchCreateLiveness = async () => {
      const response  = await fetch('http://localhost:4242/getsessionid');
      const data      = await response.json();

      setCreateLivenessApiData(data);
      setLoading(false);
    };

    fetchCreateLiveness();
  }, []);

  const handleAnalysisComplete = () => {
    fetch(
        `http://localhost:4242/processended?sessionId=${createLivenessApiData.sessionId}`
    );
  };

  return (
      <ThemeProvider>
        {loading ? (
            <Loader />
        ) : (
            <FaceLivenessDetector
                sessionId={createLivenessApiData.sessionId}
                region="eu-west-1"
                onAnalysisComplete={handleAnalysisComplete}
                disableInstructionScreen={true}
            />
        )}
      </ThemeProvider>
  );
}