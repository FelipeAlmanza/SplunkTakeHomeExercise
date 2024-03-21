import React, { useState } from 'react';
import PropTypes from 'prop-types';
import Button from '@splunk/react-ui/Button';

import { StyledContainer, StyledGreeting } from './ReactCustomTableStyles';

const propTypes = {
    name: PropTypes.string,
};

const ReactCustomTable = ({ name = 'User' }) => {
    const [counter, setCounter] = useState(0);

    const message =
        counter === 0
            ? 'You should try clicking the button.'
            : `You've clicked the button ${counter} time${counter > 1 ? 's' : ''}.`;

    return (
        <StyledContainer>
            <StyledGreeting data-testid="greeting">Hello, {name}!</StyledGreeting>
            <div>{message}</div>
            <Button
                label="Click here"
                appearance="primary"
                onClick={() => {
                    setCounter(counter + 1);
                }}
            />
        </StyledContainer>
    );
};

ReactCustomTable.propTypes = propTypes;

export default ReactCustomTable;
