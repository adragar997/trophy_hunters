export default function PaginationComponent({next, previous, onPageChange}) {

    return (
        <div className="flex justify-center gap-4">
            <button
                    onClick={() => onPageChange(previous)}
                    className="button disabled:opacity-50"
                    disabled={!previous}
                >
                    Prev
                </button>
            <button
                onClick={() => onPageChange(next)}
                className="button disabled:opacity-50"
                disabled={!next}
            >
                Next
            </button>
        </div>
    );
}