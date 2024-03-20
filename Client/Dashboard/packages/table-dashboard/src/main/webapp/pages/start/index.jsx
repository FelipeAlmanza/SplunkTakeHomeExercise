import React from 'react';

import layout from '@splunk/react-page';
import CustomTable from '@splunk/custom-table';
import { getUserTheme } from '@splunk/splunk-utils/themes';

import { StyledContainer, StyledGreeting } from './StartStyles';

getUserTheme()
    .then((theme) => {
        layout(
            <StyledContainer>
                <StyledGreeting>Hello, from inside TableDashboard!</StyledGreeting>
                <div>Your component will appear below.</div>
                <CustomTable name="from inside CustomTable" />
            </StyledContainer>,
            {
                theme,
            }
        );
    })
    .catch((e) => {
        const errorEl = document.createElement('span');
        errorEl.innerHTML = e;
        document.body.appendChild(errorEl);
    });
