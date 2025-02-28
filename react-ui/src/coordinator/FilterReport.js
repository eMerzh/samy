import {Card} from "react-bootstrap";
import React from "react";
import DatePicker from 'react-date-picker'
import Select from "react-select";
import makeAnimated from 'react-select/animated';


const FilterReport = ({reportFilterHook}) => {

    // const _ = useAppSelector(state => state.states.translation)

    const animatedComponents = makeAnimated();

    return (
        <>
            <Card style={{width: '18rem'}}>
                <Card.Header>
                    Filtres
                </Card.Header>
                <Card.Body>
                    <div className="container">
                        <div className="mb-1">
                            Status
                        </div>

                        <div className="row mb-2">
                            <div className="col">
                                <Select
                                    options={reportFilterHook?.optionsStatus.map(item => {return {value: item.value, label: item.label}})}
                                    onChange={reportFilterHook.toggleStatus}
                                    value={reportFilterHook?.filter.map(item => {return {value: item.value, label: item.label}})}
                                    components={animatedComponents}
                                    isMulti/>
                            </div>
                        </div>
                        {/*))}*/}
                        <hr/>
                        <div className="row">

                            <div className="mb-1">
                                Signalement de :
                            </div>
                            <div className="mb-2">
                                <DatePicker required={true} onChange={reportFilterHook.setDateFrom}
                                            value={reportFilterHook?.dates?.from}/>
                            </div>
                            <div className="mb-1">
                                au :
                            </div>
                            <div className="mb-2">
                                <DatePicker required={true} onChange={reportFilterHook.setDateTo}
                                            value={reportFilterHook?.dates?.to}/>
                            </div>
                        </div>
                    </div>

                </Card.Body>
            </Card>
        </>
    )
}

export default FilterReport