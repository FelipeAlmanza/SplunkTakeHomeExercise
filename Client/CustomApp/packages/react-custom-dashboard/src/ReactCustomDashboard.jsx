import React, { useEffect, useState } from 'react';
import CardLayout from '@splunk/react-ui/CardLayout';
import Card from '@splunk/react-ui/Card';

import { StyledContainer, StyledCardContent } from './ReactCustomDashboardStyles';

const ReactCustomDashboard = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://127.0.0.1:5000/overview');
                const result = await response.json();
                setData(result);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <StyledContainer>
            <CardLayout>
                {data.map((item) => (
                    <Card key={item.type}>
                        <Card.Header title={item.type} />
                        <Card.Body>
                            <StyledCardContent>Count: {item.count}</StyledCardContent>
                        </Card.Body>
                    </Card>
                ))}
            </CardLayout>
        </StyledContainer>
    );
};

export default ReactCustomDashboard;
